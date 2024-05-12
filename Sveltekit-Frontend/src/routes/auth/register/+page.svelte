<script lang="ts">
  import { KeySquare, CircleUser, SquareUser } from "lucide-svelte";
</script>

<div class="flex flex-col text-center gap-2">
  <div class="flex flex-col text-center gap-1">
    <h1 class="text-2xl">Register a New Account</h1>
    <form action="?/gotoLogin" method="POST">
      <p class="text-sm">
        Or
        <button type="submit" class="text-accent font-bold">Log in</button>
        to an Existing Account
      </p>
    </form>
  </div>

  <form
    action="?/register"
    method="POST"
    class="flex flex-col items-center space-y-2 mt-5"
    enctype="multipart/form-data"
  >
    <div class="form-control w-full max-w-md">
      <label class="input input-bordered flex items-center justify-center gap-2">
        <SquareUser class="w-4 h-4" />
        <input
          type="username"
          name="username"
          class="grow"
          placeholder="username"
        />
      </label>
    </div>
    <div class="form-control w-full max-w-md">
      <label class="input input-bordered flex items-center justify-center gap-2">
        <CircleUser class="w-4 h-4" />
        <input type="text" name="name" class="grow" placeholder="Name" />
      </label>
    </div>
    <div class="form-control w-full max-w-md">
      <label class="input input-bordered flex items-center justify-center gap-2">
        <KeySquare class="w-4 h-4" />
        <input
          type="password"
          name="password"
          class="grow"
          placeholder="Password"
          autocomplete="off"
        />
      </label>
    </div>
    <div class="form-control w-full max-w-md">
      <label class="input input-bordered flex items-center justify-center gap-2">
        <!-- <KeySquare class="w-4 h-4" /> -->
        <input
          type="file"
          name="image"
          class="grow"
          placeholder="Profile Photo"
          accept="image/*"
        />
      </label>
      
      <p class="text-xs text-primary">Upload a profile photo</p>
    </div>
    <button class="btn btn-warning btn-md w-full" type="submit"
      >Register</button
    >
  </form>
</div>
