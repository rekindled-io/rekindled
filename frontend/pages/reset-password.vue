<template>
  <div>
    <Title title="Reset password" />
    <div class="flex items-center justify-center mt-4">
      <div class="auth-form-box">
        <div class="font-bold text-lg mb-4">Reset your password below</div>
        <ValidationObserver ref="form" v-slot="{ invalid, handleSubmit }">
          <form class="space-y-8" @submit.prevent="handleSubmit()">
            <FormInput
              v-model="email"
              rules="required|email"
              label="Email"
              name="email"
              vid="email"
              required
            />
            <FormButton text="Reset" :disabled="invalid" :loading="loading" />
          </form>
        </ValidationObserver>
      </div>
    </div>
  </div>
</template>
