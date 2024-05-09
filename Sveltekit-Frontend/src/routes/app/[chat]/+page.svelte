<script lang="ts">
  import Chatbox from "$lib/chatbox/chatbox.svelte";
  import { page } from "$app/stores";
  import { onMount } from "svelte";
  let receiver = '';
  export let username: string;
  onMount(() => {
    const currenturl = $page.url.toString();
    const parts = currenturl.split("/");
    receiver = parts[parts.length-1];
  })
</script>
<div class="px-2">
  <h1 class="text-2xl">{receiver}</h1>
</div>
<Chatbox receiver={receiver} username={username}/>