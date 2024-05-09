<script lang="ts">
    import Chats from "$lib/chatbox/chats.svelte";
    export let data: any;
    const username = data.username;
    console.log("username: ", username);
  </script>
  
  <div class="flex w-3/4 h-5/6 gap-4">
    <div class="flex flex-col w-1/4 h-full overflow-hidden gap-2">
      <h1 class="text-3xl font-bold border-b-2">Chats</h1>
      <div class="w-full h-full">
        <Chats username={username}/>
      </div>
      <div class="w-full h-1/6">
        <a href="/auth/logout"><button class="btn btn-secondary btn-sm w-full">Logout</button></a>
      </div>
    </div>
    <div class="flex flex-col w-3/4 gap-2">
      <slot/>
    </div>
  </div>
  