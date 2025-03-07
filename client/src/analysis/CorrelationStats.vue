<template>
  <div class="container mx-auto">
    <h2 class="text-4xl font-bold mb-4">皮尔逊相关</h2>
    <p class="text-gray-600 dark:text-white w-full md:w-2/3 m-auto text-center text-sm md:text-2xl">
        <span class="font-bold text-indigo-500">
            “
        </span>
        主要用于量化两个连续变量之间的线性关系，适用于变量间分布较为正态、两变量均为等距或等比数值且关系大致为线性
        <span class="font-bold text-indigo-500">
            ”
        </span>
    </p>
    <form @submit.prevent="submitData" class="flex flex-col items-center">
      <div class="form-control w-full max-w-xs mb-4">
        <label class="label">
          <span class="label-text">选择自变量</span>
        </label>
        <select v-model="selectedColumn1" class="select select-bordered">
          <option disabled value="">请选择</option>
          <option v-for="column in columnOptions" :key="column" :value="column">{{ column }}</option>
        </select>
      </div>
      <div class="form-control w-full max-w-xs mb-4">
        <label class="label">
          <span class="label-text">选择因变量</span>
        </label>
        <select v-model="selectedColumn2" class="select select-bordered">
          <option disabled value="">请选择</option>
          <option v-for="column in columnOptions" :key="column" :value="column">{{ column }}</option>
        </select>
      </div>
      <button type="submit" class="btn btn-primary">提交</button>
    </form>

    <div v-if="statistics" class="mt-8">
      <div class="stats shadow">
        <div class="stat">
          <div class="stat-title">相关系数</div>
          <div class="stat-value">{{ formatNumber(statistics.correlation, 2) }}</div>
          <div class="stat-desc">{{ getCorrelationRange(statistics.correlation) }}</div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

const store = useStore();
const selectedColumn1 = ref(null);
const selectedColumn2 = ref(null);
const statistics = ref(null);
const data = computed(() => store.state.tableData);
const columnOptions = computed(() => {
  if (data.value.length > 0) {
    return Object.keys(data.value[0]);
  }
  return [];
});

const submitData = async () => {
  if (!selectedColumn1.value || !selectedColumn2.value) {
    alert('请选择一个列');
    return;
  }

  try {
    const payload = {
      column1: selectedColumn1.value,
      column2: selectedColumn2.value,
      data: store.state.tableData
    };

    const response = await axios.post('http://127.0.0.1:8000/api/corr/', payload);
    statistics.value = response.data;
  } catch (error) {
    alert('数据提交失败');
    console.error(error);
  }
};

const formatNumber = (value, decimalPlaces) => {
  return value.toFixed(decimalPlaces);
};

const getCorrelationRange = (correlation) => {
  const absCorr = Math.abs(correlation);
  if (absCorr === 0) {
    return '两个变量之间没有线性相关关系';
  } else if (absCorr >= 0.8 && absCorr <= 1) {
    return '两个变量之间存在极强的线性相关关系';
  } else if (absCorr >= 0.6 && absCorr < 0.8) {
    return '两个变量之间存在强的线性相关关系';
  } else if (absCorr >= 0.4 && absCorr < 0.6) {
    return '两个变量之间存在中等程度的线性相关关系';
  } else if (absCorr >= 0.2 && absCorr < 0.4) {
    return '两个变量之间存在弱的线性相关关系';
  } else {
    return '两个变量之间存在极弱的线性相关关系';
  }
};


</script>