<template>
  <div>
    <Title title="Reset password" />
    <div class="flex items-center justify-center mt-4">
      <div class="auth-form-box">
        <div class="mb-4 text-lg font-bold">Reset your password below</div>
        <ValidationObserver ref="form" v-slot="{ passed, handleSubmit }">
          <form class="space-y-8" @submit.prevent="handleSubmit()">
            <FormInput v-model="email" rules="required|email" label="Email" name="email" vid="email" required />
            <FormButton text="Reset" :disabled="!passed" :loading="loading" />
          </form>
        </ValidationObserver>
      </div>
    </div>
  </div>
</template>
