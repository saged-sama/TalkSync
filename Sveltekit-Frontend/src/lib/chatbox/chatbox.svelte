<script lang="ts">
  import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from "$env/static/public";
  import { SendHorizonal } from "lucide-svelte";
  import { onMount } from "svelte";

  let messages: any[] = [];
  let message: string;
  export let receiver: string;
  export let username: string;

  onMount(() => {
    getMessages();
  });

  const getMessages = async() => {
    try{
      const response = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/get-messages?chatID=${username}-${receiver}`);
      if(!response.ok){
        throw Error("Could not get messages");
      }
      const resp = await response.json();
      messages = [...resp.messages];
    } catch(err){
      console.error("Could not get messages");
    }
  }

  const addMessage = async() => {
    try{
      const response = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/add-message?chatID=${username}-${receiver}`,{
        method: "POST",
        headers: {
          "Content-type": "application/json"
        },
        body: JSON.stringify({
          message: message
        })
      });
      if(!response.ok){
        throw Error("Could not add message");
      }
      const resp = await response.json();
      messages = [...resp.messages];
    } catch(err){
      console.error("Could not add message");
    }
  }
</script>

<div
  class="flex flex-col gap-2 w-full px-5 h-full bg-neutral overflow-y-scroll"
>
  {#each messages as message}
    {#if message.sender === username}
      <div class="chat w-full chat-end">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src={message.image} />
          </div>
        </div>
        <div class="chat-header">
          {message.sender}
          <time class="text-xs opacity-50">{message.time}</time>
        </div>
        <div class="chat-bubble chat-bubble-accent">{message.message}</div>
      </div>
    {:else}
      <div class="chat w-full chat-start">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src={message.image} />
          </div>
        </div>
        <div class="chat-header">
          {message.sender}
          <time class="text-xs opacity-50">{message.time}</time>
        </div>
        <div class="chat-bubble chat-bubble-info">{message.message}</div>
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
      bind:value={message}
      on:submit={addMessage}
    />
    <button on:click={addMessage}><SendHorizonal class="h-4 w-4" /></button>
  </label>
</div>
