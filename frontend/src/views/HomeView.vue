<script setup>
import { ref, onMounted } from "vue";
import BusinessCard from "../components/BusinessCard.vue";

const currentPage = ref(1);
const nextPage = ref(null);
const previousPage = ref(null);
const businesses = ref([]);
const categories = ref([]);
const countries = ref([]);
const states = ref([]);
const loading = ref(false);
const hasLoaded = ref(false);

const selectedCategory = ref("");
const selectedCountry = ref("");
const selectedState = ref("");

const resetFilters = async () => {
  selectedCategory.value = "";
  selectedCountry.value = "";
  selectedState.value = "";
  states.value = [];
  await fetchBusinesses();
};


// Fetch businesses with all filters applied
const fetchBusinesses = async () => {
  loading.value = true;

  let url = `http://127.0.0.1:8000/api/businesses/?page=${currentPage.value}`;
  const params = [];

  if (selectedCategory.value) {
    params.push(`category=${selectedCategory.value}`);
  }

  if (selectedCountry.value) {
    params.push(`country=${selectedCountry.value}`);
  }

  if (selectedState.value) {
    params.push(`state=${selectedState.value}`);
  }

  if (params.length > 0) {
    url += "&" + params.join("&");
  }

  const response = await fetch(url);
  const data = await response.json();

  businesses.value = data.results;
  nextPage.value = data.next;
  previousPage.value = data.previous;

  loading.value = false;
  hasLoaded.value = true;
};

// Fetch categories
const fetchCategories = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/categories/");
  const data = await response.json();
  categories.value = data.results ? data.results : data;
};

// Fetch countries
const fetchCountries = async () => {
  const response = await fetch("http://127.0.0.1:8000/api/countries/");
  const data = await response.json();
  countries.value = data.results ? data.results : data;
};

// Fetch states based on selected country
const fetchStates = async () => {
  if (!selectedCountry.value) {
    states.value = [];
    return;
  }

  const response = await fetch(
    `http://127.0.0.1:8000/api/states/?country=${selectedCountry.value}`
  );

  const data = await response.json();

  // If paginated
  states.value = data.results ? data.results : data;
};


// When country changes
const handleCountryChange = async () => {
  selectedState.value = "";
  await fetchStates();
  await fetchBusinesses();
};

// When state changes
const handleStateChange = async () => {
  await fetchBusinesses();
};

// When category changes
const handleCategoryChange = async () => {
  await fetchBusinesses();
};

const goToNext = async () => {
  if (nextPage.value) {
    currentPage.value++;
    await fetchBusinesses();
  }
};

const goToPrevious = async () => {
  if (previousPage.value) {
    currentPage.value--;
    await fetchBusinesses();
  }
};

onMounted(async () => {
  await fetchCategories();
  await fetchCountries();
  await fetchBusinesses();
});
</script>

<template>
  <div>
    <h1>Explore Businesses</h1>

    <div class="filters">
      <!-- Category -->
      <select v-model="selectedCategory" @change="handleCategoryChange">
        <option value="">All Categories</option>
        <option v-for="cat in categories" :key="cat.id" :value="cat.id">
          {{ cat.name }}
        </option>
      </select>

      <!-- Country -->
      <select v-model="selectedCountry" @change="handleCountryChange">
        <option value="">All Countries</option>
        <option v-for="country in countries" :key="country.id" :value="country.id">
          {{ country.name }}
        </option>
      </select>

      <!-- State -->
      <select
        v-model="selectedState"
        @change="handleStateChange"
        :disabled="!selectedCountry"
      >
        <option value="">All States</option>
        <option v-for="state in states" :key="state.id" :value="state.id">
          {{ state.name }}
        </option>
      </select>
      <button @click="resetFilters">Reset</button>
    </div>

    <div v-if="loading">
  Loading businesses...
</div>

<div v-else-if="hasLoaded && businesses.length === 0">
  No businesses found.
</div>


    <BusinessCard
      v-for="business in businesses"
      :key="business.id"
      :business="business"
    />
    <div class="pagination">
  <button
    @click="goToPrevious"
    :disabled="!previousPage"
  >
    Previous
  </button>

  <span>Page {{ currentPage }}</span>

  <button
    @click="goToNext"
    :disabled="!nextPage"
  >
    Next
  </button>
</div>

  </div>
</template>

<style scoped>
.filters {
  margin-bottom: 20px;
  display: flex;
  gap: 15px;
}

button {
  padding: 8px 14px;
  border-radius: 6px;
  border: none;
  background-color: #1e88e5;
  color: white;
  cursor: pointer;
}

button:hover {
  background-color: #1565c0;
}

select {
  padding: 8px;
  border-radius: 6px;
  border: 1px solid #ccc;
}

h1 {
  margin-bottom: 20px;
}

.pagination {
  margin-top: 20px;
  display: flex;
  gap: 15px;
  align-items: center;
}

.pagination button {
  padding: 6px 12px;
  border-radius: 6px;
  border: none;
  background-color: #1e88e5;
  color: white;
  cursor: pointer;
}

.pagination button:disabled {
  background-color: #ccc;
  cursor: not-allowed;
}
</style>
