<script lang="ts">
  import { KeySquare, User } from "lucide-svelte";
</script>

<div class="flex flex-col text-center gap-2">
  <div class="flex flex-col text-center gap-1">
    <h1 class="text-2xl">Log in to an Account</h1>
    <form action="?/gotoRegister" method="POST">
      <p class="text-sm">
        Or
        <button type="submit" class="text-warning font-bold">Register</button>
        a New Account
      </p>
    </form>
  </div>

  <form
    action="?/login"
    method="POST"
    class="flex flex-col items-center space-y-2 mt-5"
  >
    <div class="form-control w-full max-w-md">
      <label class="input input-bordered flex items-center gap-2">
        <User class="w-4 h-4" />
        <input
          type="username"
          name="username"
          class="grow"
          placeholder="username"
        />
      </label>
    </div>
    <div class="form-control w-full max-w-md">
      <label class="input input-bordered flex items-center gap-2">
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
    <button class="btn btn-accent btn-md w-full" type="submit">Log in</button>
  </form>
</div>
