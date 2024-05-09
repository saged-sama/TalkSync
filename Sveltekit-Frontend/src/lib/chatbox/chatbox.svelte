<script lang="ts">
  let messages = [
    {
      userId: "123",
      name: "Server",
      time: "12:15",
      message: "hi",
      image:
        "https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg",
    },
    {
      userId: "123",
      name: "Server",
      time: "12:15",
      message: "hi",
      image:
        "https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg",
    },
    {
      userId: "123",
      name: "Emon",
      time: "12:15",
      message: "hi",
      image:
        "https://media.licdn.com/dms/image/D5603AQFrSXRsDj5a9A/profile-displayphoto-shrink_400_400/0/1714418121284?e=1720656000&v=beta&t=zpWTFgXJaNBxenDjASrwqfZaTG1llNn877hCJsWvmTo",
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
  const addMessage = () => {
    const newMessage = {
      userId: "123",
      name: "Emon",
      time: "9:17",
      message: "Hello friend",
      image:
        "https://img.daisyui.com/images/stock/photo-1534528741775-53994a69daeb.jpg",
    };
    messages = [...messages, newMessage];
    console.log(messages);
  };
</script>

<div
  class="flex flex-col gap-2 w-full px-5 h-full bg-neutral overflow-y-scroll"
>
  {#each messages as message}
    {#if message.name === "Emon"}
      <div class="chat w-full chat-end">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src={message.image} />
          </div>
        </div>
        <div class="chat-header">
          {message.name}
          <time class="text-xs opacity-50">{message.time}</time>
        </div>
        <div class="chat-bubble chat-bubble-accent">{message.message}</div>
        <div class="chat-footer opacity-50">Seen at 12:46</div>
      </div>
    {:else}
      <div class="chat w-full chat-start">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src={message.image} />
          </div>
        </div>
        <div class="chat-header">
          {message.name}
          <time class="text-xs opacity-50">{message.time}</time>
        </div>
        <div class="chat-bubble chat-bubble-info">{message.message}</div>
        <div class="chat-footer opacity-50">Delivered</div>
      </div>
    {/if}
  {/each}
</div>
<div class="flex justify-center w-full">
  <label class="input input-bordered flex items-center gap-2 w-full">
    <input
      type="text"
      class="grow"
      placeholder="Write a message"
      bind:value={msg}
      on:submit={addMessage}
    />
    <button on:click={addMessage}><SendHorizonal class="h-4 w-4" /></button>
  </label>
</div>
