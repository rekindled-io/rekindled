<template>
  <div class="flex justify-center items-center bg-[#f5f8ff]">
    <div class="px-2 py-12 text-gray-800 border-gray-800">
      <div class="justify-center text-center">
        <p class="text-4xl font-bold">
          <span class="border-b-4 border-gray-800">Rekindle</span>
          <span class="text-">lost gaming friendships</span>
        </p>
        <div class="my-4">
          Rekindled is a repository of gaming handles that enables you to
          reconnect with old friends.
          <p>
            Try it out by searching for an old friend below, or
            <Nuxt-Link class="font-semibold" to="/register">Register</Nuxt-Link>
            an account to get started.
          </p>
        </div>
        <div class="w-1/2 pt-8">
          <form @submit.prevent="submit">
            <FormInput icon="search" label="Search for an old friend..." />
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
div >>> input {
  @apply border-black;
  @apply text-lg;
}
div >>> label {
  @apply text-gray-700;
}
</style>
