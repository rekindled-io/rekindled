<template>
  <nav class="bg-gray-800 border-b-2 border-black">
    <div class="max-w-6xl mx-auto py-3">
      <div class="flex items-center justify-between">
        <div class="flex flex-col items-center font-semibold text-white">
          <Logo />
        </div>
        <div>
          <NuxtLink to="/search">
            <div
              class="text-lg font-bold text-gray-800 tracking-wide hover:text-yellow-300 hover:underline"
            >
              search
            </div>
          </NuxtLink>
        </div>

        <div class="flex ml-4 items-center md:ml-6">
          <div class="space-x-2">
            <Nuxt-Link
              tag="button"
              to="/login"
              type="button"
              class="bg-transparent border text-white font-semibold text-sm rounded px-4 py-1.5 transform hover:-translate-y-0.5 transition duration-200"
            >
              Login
            </Nuxt-Link>
            <Nuxt-Link
              tag="button"
              to="/register"
              type="button"
              class="bg-yellow-400 font-semibold text-sm rounded px-4 py-1.5 text-black transform hover:-translate-y-0.5 transition duration-200"
              >Register
            </Nuxt-Link>
          </div>
        </div>
      </div>
    </div>
  </nav>
</template>
