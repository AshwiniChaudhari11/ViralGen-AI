const API = "http://127.0.0.1:8000";

/* ================= COPY GENERATION ================= */

async function generateCopy() {
    const desc = document.getElementById("desc");
    const platform = document.getElementById("platform");
    const persona = document.getElementById("persona");

    const btn = document.getElementById("copyBtn");
    const output = document.getElementById("copyOutput");

    // Validation
    if (!desc.value.trim()) {
        output.innerText = "⚠️ Please enter a product description";
        return;
    }

    // Loading state
    btn.innerText = "Generating... ✨";
    btn.disabled = true;
    output.innerText = "Creating high-quality marketing copy...";

    try {
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

        if (data.generated_copy) {
            output.innerText = data.generated_copy;
        } else {
            output.innerText = "❌ Failed to generate copy";
        }

    } catch (error) {
        console.error(error);
        output.innerText = "❌ Error connecting to server";
    }

    // Reset button
    btn.innerText = "✨ Generate Copy";
    btn.disabled = false;
}


/* ================= IMAGE GENERATION ================= */

async function generateImage() {
    const input = document.getElementById("imageDesc");
    const btn = document.getElementById("imgBtn");
    const status = document.getElementById("imageStatus");

    // Validation
    if (!input.value.trim()) {
        status.innerText = "⚠️ Please describe the image";
        return;
    }

    // Loading state
    btn.innerText = "Generating... 🎨";
    btn.disabled = true;
    status.innerText = "🧠 AI is generating image... please wait";

    try {
        const res = await fetch(`${API}/generate-image-async`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({
                product_description: input.value
            })
        });

        const data = await res.json();

        if (data.job_id) {
            checkStatus(data.job_id, btn);
        } else {
            status.innerText = "❌ Failed to start image generation";
            btn.innerText = "✨ Generate Image";
            btn.disabled = false;
        }

    } catch (error) {
        console.error(error);
        status.innerText = "❌ Server error";
        btn.innerText = "✨ Generate Image";
        btn.disabled = false;
    }
}


/* ================= CHECK IMAGE STATUS ================= */

async function checkStatus(jobId, btn) {
    const status = document.getElementById("imageStatus");

    const interval = setInterval(async () => {
        try {
            const res = await fetch(`${API}/job-status/${jobId}`);
            const data = await res.json();

            status.innerText = "Status: " + data.status;

            /* ✅ IMAGE READY */
            if (data.status === "completed" && data.image_url) {

                clearInterval(interval);

                status.innerText = "✅ Image Ready!";

                const imageUrl = data.image_url.image_url;

                const preview = document.getElementById("previewImage");
                const resultBox = document.getElementById("imageResult");
                const downloadBtn = document.getElementById("downloadBtn");

                // Show image
                preview.src = imageUrl;
                resultBox.style.display = "block";

                // Click to open full image
                preview.onclick = () => {
                    window.open(imageUrl, "_blank");
                };

                // Download functionality
                downloadBtn.onclick = async () => {
                    try {
                        const response = await fetch(imageUrl);
                        const blob = await response.blob();

                        const url = window.URL.createObjectURL(blob);

                        const a = document.createElement("a");
                        a.href = url;
                        a.download = "viralgen-image.png";

                        document.body.appendChild(a);
                        a.click();

                        a.remove();
                        window.URL.revokeObjectURL(url);

                    } catch (err) {
                        alert("❌ Download failed");
                    }
                };

                // Reset button
                btn.innerText = "✨ Generate Image";
                btn.disabled = false;
            }

            /* ❌ FAILED */
            if (data.status === "failed") {
                clearInterval(interval);
                status.innerText = "❌ Image generation failed";
                btn.innerText = "✨ Generate Image";
                btn.disabled = false;
            }

        } catch (error) {
            console.error(error);
            clearInterval(interval);
            status.innerText = "❌ Error checking status";
            btn.innerText = "✨ Generate Image";
            btn.disabled = false;
        }

    }, 3000);
}