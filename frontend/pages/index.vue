<template>
  <div>
    <LayoutHero />
    <Heading content="Most Popular" />
    <Loading v-if="$fetchState.pending && !games.length" />
    <section v-else class="grid w-full grid-cols-2 px-4 mx-auto my-8 sm:grid-cols-4 lg:grid-cols-5 gap-x-4 xl:w-2/3">
      <CardsGame v-for="(game, index) in games" :data="game" :index="index" :key="game.name" />
    </section>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { Game } from '~/modules/game/Game';

export default Vue.extend({
  data() {
    return {
      games: [] as Game[]
    };
  },

  async fetch() {
    this.games = await this.$services.game.ranking();
  }
});
</script>
