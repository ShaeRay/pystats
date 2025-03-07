<template>
  <div class="container mx-auto">
    <h2 class="text-4xl font-bold mb-4">假设检验 - 单因素方差分析</h2>
    <p class="text-gray-600 dark:text-white w-full md:w-2/3 m-auto text-center text-lg md:text-3xl">
      <span class="font-bold text-indigo-500">“ </span>
      在研究中，单因素方差分析(ANOVA)可以帮助我们理解不同组之间是否存在显著差异。
      <span class="font-bold text-indigo-500"> ”</span>
    </p>

     <form @submit.prevent="submitData" class="flex flex-col items-center pt-10">
      <!-- 第一个选择框用于选择性别 -->
      <div class="form-control w-full max-w-xs mb-4">
        <label class="label">
          <span class="label-text">请选择性别列 (Gender)</span>
        </label>
        <select v-model="selectedColumn1" class="select select-bordered">
          <option disabled value="">请选择性别</option>
          <option v-for="column in columnOptions" :key="column" :value="column">{{ column }}</option>
        </select>
      </div>

      <!-- 第二个选择框用于选择成绩科目 -->
      <div class="form-control w-full max-w-xs mb-4">
        <label class="label">
          <span class="label-text">请选择成绩科目</span>
        </label>
        <select v-model="selectedColumn2" class="select select-bordered">
          <option disabled value="">请选择科目</option>
          <option v-for="column in columnOptions" :key="column" :value="column">{{ column }}</option>
        </select>
      </div>

      <button type="submit" class="btn btn-primary">提交</button>
    </form>

     <div v-if="statistics" class="mt-8">
      <div class="stats shadow grid grid-cols-2 gap-4">
        <div class="stat">
          <div class="stat-title">F 检验</div>
          <div class="stat-value">{{ formatNumber(statistics.f_statistic, 4) }}</div>
        </div>
        <div class="stat">
          <div class="stat-title">p 值</div>
          <div class="stat-value">{{ formatNumber(statistics.p_value, 4) }}</div>
        </div>
      </div>
      <div class="explanation mt-4 p-4 border rounded">
        <p><strong>F检验结果：</strong> 
          我们的单因素方差分析（ANOVA）返回的F检验统计值为<strong>{{ formatNumber(statistics.f_statistic, 4) }}</strong>。
          这个结果表明在零假设（所有组的总体均值相等）成立的前提下，观察到的数据存在{{ statistics.p_value < 0.05 ? '显著的' : '不显著的' }}组间差异。
        </p>
        <p>
          <strong>p值分析：</strong>分析的p值为<strong>{{ formatNumber(statistics.p_value, 4) }}</strong>，
          {{ statistics.p_value < 0.05 ? '小于' : '大于或等于' }}常用的显著性水平0.05。
          这个结果{{ statistics.p_value < 0.05 ? '拒绝了' : '没有拒绝' }}原假设，即所有组的总体均值相等。
          因此，我们有{{ statistics.p_value < 0.05 ? '有' : '没有' }}足够的证据认为，观察到的统计差异并不仅是随机误差产生，而是{{ statistics.p_value < 0.05 ? '真实存在' : '不存在' }}。
        </p>
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

    const response = await axios.post('http://127.0.0.1:8000/api/anova/', payload);
    statistics.value = response.data;
  } catch (error) {
    alert('数据提交失败');
    console.error(error);
  }
};

const formatNumber = (value, decimalPlaces) => {
  if (value !== null && !isNaN(value)) {
    return value.toFixed(decimalPlaces);
  }
  return 'N/A';
};

</script>