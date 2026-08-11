import useVoiceCommand from '../hooks/useVoiceCommand';

function VoiceCommand({ onCommandSuccess }) {
  const { response, loading, error, sendCommand } = useVoiceCommand({
    onSuccess: onCommandSuccess,
  });

  return (
    <div className="VoiceCommand">
      <button onClick={sendCommand} disabled={loading}>
        {loading ? 'Escuchando...' : 'Enviar comando de voz'}
      </button>
      {error && <p className="VoiceCommand-error">{error}</p>}
      {!error && response && <p>Respuesta: {response}</p>}
    </div>
  );
}

export default VoiceCommand;
