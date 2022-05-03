<template>
  <div>
    <LayoutHero />
    <Heading content="Most Popular" />
    <Loading v-if="$fetchState.pending && !games.length" />
    <section v-else class="grid grid-cols-2 px-4 sm:grid-cols-4 lg:grid-cols-5 gap-x-4 w-full xl:w-2/3 my-8 mx-auto">
      <div v-for="(game, index) in games.results" :key="game.name" class="flex">
        <CardsGame :data="game" :index="index" />
      </div>
    </section>
  </div>
</template>

<script lang="ts">
import Vue from 'vue';
import { GameList } from '~/modules/game/Game';

export default Vue.extend({
  data() {
    return {
      games: {} as GameList
    };
  },
  async fetch() {
    this.games = await this.$services.game.list();
  }
});
</script>
