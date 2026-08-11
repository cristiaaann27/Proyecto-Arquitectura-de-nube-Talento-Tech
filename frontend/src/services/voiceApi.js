import apiClient from './api';

export async function sendVoiceCommand() {
  const res = await apiClient.post('/voice-command', {});
  return res.data;
}
