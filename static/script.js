const API = "http://127.0.0.1:8000";

/* TEXT GENERATION */
async function generateCopy() {

    const data = {
        product_description: document.getElementById("desc").value,
        platform: document.getElementById("platform").value,
        persona: document.getElementById("persona").value
    };

    const res = await fetch(`${API}/generate-copy`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(data)
    });

    const result = await res.json();

    document.getElementById("copyOutput").innerText =
        result.generated_copy;
}


/* IMAGE GENERATION */
async function generateImage() {

    const desc = document.getElementById("imageDesc").value;

    const res = await fetch(`${API}/generate-image-async`, {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify({
            product_description: desc
        })
    });

    const data = await res.json();

    checkStatus(data.job_id);
}


async function checkStatus(jobId) {

    const statusDiv = document.getElementById("imageStatus");

    const interval = setInterval(async () => {

        const res = await fetch(`${API}/job-status/${jobId}`);
        const data = await res.json();

        statusDiv.innerText = "Status: " + data.status;

        if (data.image_url) {
            document.getElementById("resultImage").src =
                data.image_url;
            clearInterval(interval);
        }

    }, 3000);
}