import { useCallback, useState } from 'react';

import { sendVoiceCommand } from '../services/voiceApi';

export default function useVoiceCommand({ onSuccess } = {}) {
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendCommand = useCallback(async () => {
    setLoading(true);
    setError(null);
    try {
      const data = await sendVoiceCommand();
      setResponse(data.message);
      onSuccess?.();
    } catch (err) {
      setError('Error al procesar el comando de voz');
    } finally {
      setLoading(false);
    }
  }, [onSuccess]);

  return { response, loading, error, sendCommand };
}
