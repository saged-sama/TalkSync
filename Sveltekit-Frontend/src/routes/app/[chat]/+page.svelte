<script lang="ts">
  import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from "$env/static/public";
  import { SendHorizonal } from "lucide-svelte";
  import { onDestroy, onMount } from "svelte";

  export let data: any;
  const { props } = data;
  const { receiver, username } = props;
  let message: string;
  let messages: any[] = [];
  let receiverProfilePic: string;
  let senderProfilePic: string;

  const getMessages = async () => {
    if(!username || !receiver){
      return;
    }
    try {
      const response = await fetch(
        `http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/get-messages?chatID=${username}-${receiver}`
      );
      if (!response.ok) {
        throw Error("Could not get messages");
      }
      const resp = await response.json();
      messages = [...resp.messages]
    } catch (err) {
      console.error("Could not get messages: ", err);
    }
  };

  const addMessage = async () => {
    console.log("ASAS")
    if (message === "") {
      return;
    }
    try {
      const response = await fetch(
        `http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/add-message?chatID=${username}-${receiver}`,
        {
          method: "POST",
          headers: {
            "Content-type": "application/json",
          },
          body: JSON.stringify({
            sender: username,
            message: message,
            image: "",
          }),
        }
      );
      if (!response.ok) {
        throw Error("Could not add message");
      }
      const resp = await response.json();
      messages = [...resp.messages];
      message = ''
    } catch (err) {
      console.error("Could not add message: ", err);
    }
  };

  const getProfilePic = async(username: string) => {
    try{
      const response = await fetch(`http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/get-image-path?username=${username}`);
      if(!response.ok){
        throw Error("Could not get profile pic");
      }
      const resp = await response.json();
      const imagepath = resp.imagepath;
      return `http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/get-file?path=${imagepath}`;
    }
    catch(err){
      console.error("Could not get profile pic: ", err);
      return "";
    }
  }
  let interval: any;
  onMount(async() => {
    receiverProfilePic = await getProfilePic(receiver);
    senderProfilePic = await getProfilePic(username);
    getMessages();
    interval = setInterval(getMessages, 1000);
  })
  onDestroy(() => {
    clearInterval(interval);
  })
</script>

<div class="px-2">
  <h1 class="text-2xl">{receiver}</h1>
</div>
<div
  class="flex flex-col-reverse gap-2 w-full p-5 h-full bg-neutral overflow-y-scroll"
>
  {#each messages.slice().reverse() as mssg}
    {#if mssg.sender === username}
      <div class="flex flex-col gap-2 chat w-full chat-end">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src={senderProfilePic} />
          </div>
        </div>
        <div class="chat-header px-5 text-xl font-bold">
          {mssg.sender}
        </div>
        <div class="flex flex-col gap-2 chat-bubble chat-bubble-accent">
          <p>{mssg.message}</p>
          <time class="opacity-50 text-xs">{mssg.time}</time>
        </div>
      </div>
    {:else}
      <div class="flex flex-col chat w-full chat-start gap-2">
        <div class="chat-image avatar">
          <div class="w-10 rounded-full">
            <img alt="Tailwind CSS chat bubble component" src={receiverProfilePic} />
          </div>
        </div>
        <div class="chat-header px-5 text-xl font-bold">
          {mssg.sender}
        </div>
        <div class="flex flex-col gap-2 chat-bubble chat-bubble-info">
          <p>{mssg.message}</p>
          <time class="text-xs opacity-50">{mssg.time}</time>
        </div>
      </div>
    {/if}
  {/each}
</div>
<div class="flex justify-center w-full">
  <label class="input input-bordered w-full flex items-center gap-2">
    <input
      type="text"
      class="grow"
      placeholder="Write a message"
      on:keydown={(event)=>{
        if(event.key === "Enter"){
          event.preventDefault();
          addMessage();
        }
      }}
      bind:value={message}
      name="message"
    />
    <button on:click={addMessage} class="btn btn-ghost btn-sm"
      ><SendHorizonal class="h-4 w-4" /></button
    >
  </label>
</div>
