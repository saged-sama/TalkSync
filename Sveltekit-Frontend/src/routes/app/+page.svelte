<script>
  import Chatbox from "$lib/chatbox/chatbox.svelte";
  import Chats from "$lib/chatbox/chats.svelte";
</script>

<div class="flex w-3/4 h-5/6 gap-4">
  <div class="flex flex-col w-1/4 h-full overflow-hidden gap-2">
    <h1 class="text-3xl font-bold border-b-2">Chats</h1>
    <Chats />
  </div>
  <div class="flex flex-col w-3/4 gap-2">
    <div class="px-2">
      <h1 class="text-2xl">Server</h1>
    </div>
    <Chatbox />
  </div>
</div>
