<script>
    let messages = [
        {
            userId: "123",
            name: "Server",
            time: "12:15",
            message:
                "Hello whacsd ckadckhbhakbcts'up ajbdjkad hajk s d abdkcadc",
            image: "https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg",
        },
        {
            userId: "123",
            name: "Emon",
            time: "12:15",
            message: "Hello from Serverdaedabdak ajbaked jdabeidka edaved",
            image: "https://media.licdn.com/dms/image/D5603AQFrSXRsDj5a9A/profile-displayphoto-shrink_400_400/0/1714418121284?e=1720656000&v=beta&t=zpWTFgXJaNBxenDjASrwqfZaTG1llNn877hCJsWvmTo",
        },
    ];
    let msg = "";
    let userID = "123";
    let chatID = "789";
    import { SendHorizonal } from "lucide-svelte";

    const send = async () => {
        console.log("fa");
        try {
            const res = await fetch(`http://localhost:8000/post-message`, {
                method: "POST",
                credentials: "include",
                headers: {
                    "Content-type": "application/json",
                },
                body: JSON.stringify({
                    chatID: chatID,
                    userID: userID,
                    message: msg,
                }),
            });
            console.log(res);
            const item = await res.json();
        } catch (e) {
            console.log(e);
        }
    };
</script>

<div class="flex flex-col">
    {#each messages as message}
        <div class="flex items-start gap-2.5 mb-4">
            <!-- svelte-ignore a11y-img-redundant-alt -->
            {#if message.name != "Emon"}
                <!-- svelte-ignore a11y-img-redundant-alt -->
                <img
                    class="w-8 h-8 rounded-full"
                    src={message.image}
                    alt="Jese image"
                />
            {/if}
            {#if message.name == "Emon"}
                <button
                    id="dropdownMenuIconButton"
                    data-dropdown-toggle="dropdownDots"
                    data-dropdown-placement="bottom-start"
                    class="inline-flex self-center items-center p-2 text-sm font-medium text-center text-gray-900 bg-white rounded-lg hover:bg-gray-100 focus:ring-4 focus:outline-none dark:text-white focus:ring-gray-50 dark:bg-gray-900 dark:hover:bg-gray-800 dark:focus:ring-gray-600"
                    type="button"
                >
                    <svg
                        class="w-4 h-4 text-gray-500 dark:text-gray-400"
                        aria-hidden="true"
                        xmlns="http://www.w3.org/2000/svg"
                        fill="currentColor"
                        viewBox="0 0 4 15"
                    >
                        <path
                            d="M3.5 1.5a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 6.041a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Zm0 5.959a1.5 1.5 0 1 1-3 0 1.5 1.5 0 0 1 3 0Z"
                        />
                    </svg>
                </button>
            {/if}
            <div
                class="flex flex-col w-full max-w-[320px] leading-1.5 p-4 border-gray-200 bg-gray-100 rounded-e-xl rounded-es-xl dark:bg-gray-700"
            >
                <div class="flex items-center space-x-2 rtl:space-x-reverse">
                    <span
                        class="text-sm font-semibold text-gray-900 dark:text-white"
                        >{message.name}</span
                    >
                    <span
                        class="text-sm font-normal text-gray-500 dark:text-gray-400"
                        >{message.time}</span
                    >
                </div>
                <p
                    class="text-sm font-normal py-2.5 text-gray-900 dark:text-white"
                >
                    {message.message}
                </p>
                <span
                    class="text-sm font-normal text-gray-500 dark:text-gray-400"
                    >Delivered</span
                >
            </div>
            {#if message.name == "Emon"}
                <!-- svelte-ignore a11y-img-redundant-alt -->
                <img
                    class="w-8 h-8 rounded-full"
                    src={message.image}
                    alt="Jese image"
                />
            {/if}
        </div>
    {/each}
    <label class="input input-bordered flex items-center gap-2">
        <input type="text" class="grow" placeholder="Search" bind:value={msg} />
        <button on:click={send}><SendHorizonal class="h-4 w-4" /></button>
    </label>
</div>
