import { render, screen } from '@testing-library/react';

import App from './App';
import * as taskApi from './services/taskApi';

jest.mock('./services/taskApi');
jest.mock('./services/voiceApi');

beforeEach(() => {
  taskApi.getTasks.mockResolvedValue([]);
});

test('renders the app heading and task list once loaded', async () => {
  render(<App />);

  expect(screen.getByText(/voice command task assistant/i)).toBeInTheDocument();
  expect(await screen.findByText(/no tienes tareas/i)).toBeInTheDocument();
});

test('renders the voice command button', async () => {
  render(<App />);

  expect(screen.getByRole('button', { name: /enviar comando de voz/i })).toBeInTheDocument();
  await screen.findByText(/no tienes tareas/i);
});
