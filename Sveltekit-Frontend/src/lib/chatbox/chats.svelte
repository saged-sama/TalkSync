<script lang="ts">
  import { PUBLIC_SERVER_HOST, PUBLIC_SERVER_PORT } from "$env/static/public";
  import { onMount } from "svelte";

  export let username: string;
  let searchuser: string = "";
  let searchresults: any[] = [];
  let users: any[] = [];

  const search = async () => {
    if (searchuser === "") {
      return;
    }
    try {
      const response = await fetch(
        `http://localhost:8000/search-username?user=${searchuser}`,
        {
          method: "GET",
          credentials: "include",
        }
      );
      if (!response.ok) {
        throw Error("Could not search username");
      }
      const res = await response.json();
      searchresults = [...res.users];
    } catch (err) {
      console.error("Could not search username");
    }
  };

  onMount(() => {
    console.log("Username: ", username);
    const getUsers = async () => {
      try {
        const response = await fetch(
          `http://${PUBLIC_SERVER_HOST}:${PUBLIC_SERVER_PORT}/get-users`
        );
        if (!response.ok) {
          throw Error("Could not get users");
        }
        const resp = await response.json();
        users = [...resp.users];
      } catch (err) {
        console.error("Could not get users");
      }
    };
    getUsers();
  });
</script>

<div class="h-full w-full overflow-y-auto">
  <ul class="menu p-4 w-full h-full bg-base-200 text-base-content">
    {#each users as user}
      {#if user.username !== username}
        <li class="bg-neutral"><a href={`/app/${user.username}`}>{user.name}</a></li>
      {/if}
    {/each}
  </ul>
</div>
