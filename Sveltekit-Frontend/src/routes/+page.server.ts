export async function load() {
    const res = await fetch(`http://127.0.0.1:8000/post-message`, 
            {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    message: "Hello from frontend"
                })
            }
        );
        const item = await res.json();
        return {item};
}