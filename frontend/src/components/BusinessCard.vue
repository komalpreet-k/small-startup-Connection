<script setup>
import { useRouter } from "vue-router";

const props = defineProps({
  business: Object
});

const router = useRouter();

const goToDetail = () => {
  router.push(`/business/${props.business.id}`);
};
</script>

<template>
  <div class="card" @click="goToDetail">
    <h3>{{ business.name }}</h3>
    <p>{{ business.description }}</p>
    <p class="location">
      {{ business.city.name }}, {{ business.state.name }}
    </p>
  </div>
</template>

<style scoped>
.card {
  background: white;
  padding: 20px;
  margin-bottom: 15px;
  border-radius: 8px;
  box-shadow: 0 2px 6px rgba(0,0,0,0.1);
  cursor: pointer;
  transition: 0.2s;
}

.card:hover {
  transform: translateY(-3px);
}

.location {
  color: gray;
  font-size: 14px;
}
</style>
