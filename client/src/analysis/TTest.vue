<template>
  <div class="container mx-auto">
    <h2 class="text-4xl font-bold mb-4">T检验</h2>
    <p class="text-gray-600 dark:text-white w-full md:w-2/3 m-auto text-center text-sm md:text-2xl">
        <span class="font-bold text-indigo-500">
            “
        </span>
        主要用于比较两组数据的平均值是否有显著性差异
        <span class="font-bold text-indigo-500">
            ”
        </span>
    </p>

    <form @submit.prevent="submitData" class="flex flex-col items-center pt-10">
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
      <div class="stats shadow grid grid-cols-2 gap-4">
        <div class="stat">
          <div class="stat-title">t检验</div>
          <div class="stat-value">{{ formatNumber(statistics.t_statistic, 4) }}</div>
        </div>
        <div class="stat">
          <div class="stat-title">p值</div>
          <div class="stat-value">{{ formatNumber(statistics.p_value, 4) }}</div>
        </div>
      </div>
      <div class="explanation mt-4 p-4 border rounded">
        <p>
          t值主要反映了自变量与因变量之间关联的程度，
        </p>
        <p>
          本研究中进行的t检验所得到的统计量值为 <strong>{{ formatNumber(statistics.t_statistic, 4) }}</strong>。
        </p>
        <p>
          此结果{{ statistics.t_statistic ? '指明' : '未表明' }}，在零假设（两组样本的总体均值相等）成立的前提下，
        </p>
        <p>
          自变量与因变量之间的差异{{ statistics.t_statistic && statistics.t_statistic > 2 || statistics.t_statistic < -2 ? '不显著' : '显著' }}。
        </p>
        <br>
        <p>
          <strong>p值分析：</strong>相应的p值为 <strong>{{ formatNumber(statistics.p_value, 4) }}</strong>，{{ statistics.p_value < 0.05 ? '低于' : '高于或等于' }}常用的显著性水平0.05。
        </p>
        <p>
          这{{ statistics.p_value < 0.05 ? '暗示' : '并不意味着' }}原假设可被拒绝，即两组样本的总体均值在统计上{{ statistics.p_value < 0.05 ? '具有显著差异' : '无显著差异' }}。
        </p>
        <p>
          因此，我们{{ statistics.p_value < 0.05 ? '有' : '没有' }}充分的证据认为，观测到的均值差异超出了随机误差的范围，揭示了两组样本之间的{{ statistics.p_value < 0.05 ? '实际效应' : '无显著不同' }}。
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

    const response = await axios.post('http://127.0.0.1:8000/api/ttest/', payload);
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