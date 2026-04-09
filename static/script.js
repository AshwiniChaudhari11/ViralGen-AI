const API = "http://127.0.0.1:8000";

/* ================= COPY GENERATION ================= */

async function generateCopy() {

    const desc = document.getElementById("desc");
    const platform = document.getElementById("platform");
    const persona = document.getElementById("persona");

    document.getElementById("copyOutput").innerText =
        "Generating copy... ✨";

    const res = await fetch(`${API}/generate-copy`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            product_description: desc.value,
            platform: platform.value,
            persona: persona.value
        })
    });

    const data = await res.json();

    document.getElementById("copyOutput").innerText =
        data.generated_copy;
}


/* ================= IMAGE GENERATION ================= */

async function generateImage() {

    const status = document.getElementById("imageStatus");

    status.innerText = "🧠 AI is generating image...";

    const res = await fetch(`${API}/generate-image-async`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
            product_description:
                document.getElementById("imageDesc").value
        })
    });

    const data = await res.json();

    checkStatus(data.job_id);
}


/* ================= CHECK IMAGE STATUS ================= */

async function checkStatus(jobId) {

    const status = document.getElementById("imageStatus");

    const interval = setInterval(async () => {

        const res = await fetch(`${API}/job-status/${jobId}`);
        const data = await res.json();

        status.innerText = "Status: " + data.status;

        /* ✅ IMAGE READY CONDITION */
        if (data.status === "completed" && data.image_url) {

            clearInterval(interval);

            status.innerText = "✅ Image Ready!";

            // IMPORTANT: correct path from backend response
            const imageUrl = data.image_url.image_url;

            const preview =
                document.getElementById("previewImage");

            const resultBox =
                document.getElementById("imageResult");

            const downloadBtn =
                document.getElementById("downloadBtn");

            /* ---- Show Thumbnail ---- */
            preview.src = imageUrl;
            resultBox.style.display = "block";

            /* ---- Open Full Image ---- */
            preview.onclick = () => {
                window.open(imageUrl, "_blank");
            };

            /* ---- Download Fix ---- */
            downloadBtn.onclick = async () => {

                const response = await fetch(imageUrl);
                const blob = await response.blob();

                const url =
                    window.URL.createObjectURL(blob);

                const a = document.createElement("a");
                a.href = url;
                a.download = "viralgen-image.png";

                document.body.appendChild(a);
                a.click();

                a.remove();
                window.URL.revokeObjectURL(url);
            };
        }

    }, 3000);
}