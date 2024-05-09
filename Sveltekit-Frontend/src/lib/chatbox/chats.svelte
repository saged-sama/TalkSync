<script lang="ts">
    let searchuser: string = "";
    let searchresults = [];

    const search = async() => {
        if(searchuser === ""){
            return;
        }
        try{
            const response = await fetch(`http://localhost:8000/search-username?user=${searchuser}`, {
                method: "GET",
                credentials: "include"
            });
            if(!response.ok){
                throw Error("Could not search username");
            }
            const res = await response.json();
            searchresults = [...res.users];
            console.log("SearchRes: ", searchresults);
        }catch(err){
            console.error("Could not search username");
        }
    };

</script>

<div class="drawer lg:drawer-open">
    <input id="my-drawer-2" type="checkbox" class="drawer-toggle" />
    <div class="drawer-side">
      <label for="my-drawer-2" aria-label="close sidebar" class="drawer-overlay"></label>
      <input type="text" class="input input-bordered input-info input-sm w-3/4" placeholder="Search" on:change={search} bind:value={searchuser}>
      <ul class="menu p-4 w-80 min-h-full bg-base-200 text-base-content overflow-y-scroll">
        <li><a href="/app/">Sidebar Item 1</a></li>
        <li><a href="/app/">Sidebar Item 2</a></li>
      </ul>
    </div>
</div>