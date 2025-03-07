<template>
    <section>
        <div class="mx-auto w-full max-w-7xl px-5  md:px-10">
            <h1 class="text-4xl font-bold mb-4">描述统计</h1>
            <p class="text-gray-600 dark:text-white w-full md:w-2/3 m-auto text-center text-sm md:text-2xl">
                <span class="font-bold text-indigo-500">
                    “
                </span>
                主要用于描述统计概括数据集的中心趋势、分散和形状特征
                <span class="font-bold text-indigo-500">
                    ”
                </span>
            </p>


            <form @submit.prevent="submitData">
                <div class="mb-4">
                    <label for="column-select" class="block mb-2">选择列</label>
                    <select id="column-select" v-model="selectedColumn" class="select select-bordered w-full max-w-xs">
                    <option disabled value="">请选择</option>
                    <option v-for="column in columnOptions" :key="column" :value="column">{{ column }}</option>
                    </select>
                </div>
                <button type="submit" class="btn btn-primary">提交</button>
            </form>
        </div>
    </section>

    <section>
        <div v-if="statistics" class="container mx-auto stats shadow mt-8">
            <div class="stats-grid grid grid-cols-1 sm:grid-cols-2 md:grid-cols-3 gap-4">
                <div class="stat">
                    <div class="stat-title">平均值</div>
                    <div class="stat-value">{{ formatNumber(statistics.mean, 1) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">中位数</div>
                    <div class="stat-value">{{ formatNumber(statistics.median, 1) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">标准差</div>
                    <div class="stat-value">{{ formatNumber(statistics.std_dev, 2) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">方差</div>
                    <div class="stat-value">{{ formatNumber(statistics.variance, 2) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">最小值</div>
                    <div class="stat-value">{{ formatNumber(statistics.min, 1) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">最大值</div>
                    <div class="stat-value">{{ formatNumber(statistics.max, 1) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">全距</div>
                    <div class="stat-value">{{ formatNumber(statistics.range, 1) }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">四分位数</div>
                    <div class="stat-value">{{ statistics.quartiles.join(', ') }}</div>
                </div>
                <div class="stat">
                    <div class="stat-title">是否符合正态分布</div>
                    <div class="stat-value">{{ statistics.is_normal ? '是' : '否' }}</div>
                </div>
            </div>
        </div>
    </section>
</template>

<script setup>
import { ref, computed } from 'vue';
import { useStore } from 'vuex';
import axios from 'axios';

const store = useStore();
const selectedColumn = ref(null);
const statistics = ref(null);
const data = computed(() => store.state.tableData);
const columnOptions = computed(() => {
  if (data.value.length > 0) {
    return Object.keys(data.value[0]);
  }
  return [];
});

const submitData = async () => {
  if (!selectedColumn.value) {
    alert('请选择一个列');
    return;
  }

  try {
    const payload = {
      column: selectedColumn.value,
      data: store.state.tableData
    };
    const response = await axios.post('http://127.0.0.1:8000/api/stats/', payload);
    statistics.value = response.data;
  } catch (error) {
    alert('数据提交失败');
    console.error(error);
  }
};

const formatNumber = (value, decimalPlaces) => {
  return value.toFixed(decimalPlaces);
};
</script>
