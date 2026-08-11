import apiClient from './api';

export async function getTasks() {
  const res = await apiClient.get('/tasks');
  return res.data.tasks;
}

export async function createTask(payload) {
  const res = await apiClient.post('/tasks', payload);
  return res.data;
}

export async function updateTask(id, payload) {
  const res = await apiClient.put(`/tasks/${id}`, payload);
  return res.data;
}

export async function deleteTask(id) {
  const res = await apiClient.delete(`/tasks/${id}`);
  return res.data;
}
