<script setup>
import { useRouter } from "vue-router";

const props = defineProps({
  business: Object
});

const router = useRouter();

const goToDetail = () => {
  router.push(`/business/${props.business.id}`);
};

const saveBusiness = async (event) => {
  // Prevent card click navigation
  event.stopPropagation();

  const token = localStorage.getItem("access_token");

  if (!token) {
    alert("Please login to save businesses.");
    router.push("/login");
    return;
  }

  try {
    const response = await fetch(
      "http://127.0.0.1:8000/api/saved-businesses/",
      {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
        body: JSON.stringify({
          business: props.business.id,
        }),
      }
    );

    if (!response.ok) {
      throw new Error("Failed to save");
    }

    alert("Business saved successfully!");
  } catch (error) {
    console.error(error);
    alert("Error saving business.");
  }
};
</script>

<template>
  <div class="card" @click="goToDetail">
    <h3>{{ business.name }}</h3>
    <p>{{ business.description }}</p>
    <p class="location">
      {{ business.city.name }}, {{ business.state.name }}
    </p>

    <button class="save-btn" @click="saveBusiness">
      Save
    </button>
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
  position: relative;
}

.card:hover {
  transform: translateY(-3px);
}

.location {
  color: gray;
  font-size: 14px;
}

.save-btn {
  margin-top: 10px;
  padding: 6px 12px;
  background-color: #1e88e5;
  color: white;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

.save-btn:hover {
  background-color: #1565c0;
}
</style>
