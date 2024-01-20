// setupTests.js

import '@testing-library/jest-dom';
import { configure } from '@testing-library/react';

// Extend Jest matchers to use additional DOM assertions
configure({ testIdAttribute: 'data-testid' });

// Mocking the global.fetch included in Jest to handle the API calls in the tests
global.fetch = jest.fn(() =>
  Promise.resolve({
    json: () => Promise.resolve({}),
  })
);

beforeEach(() => {
  // Clear all mocks before each test
  jest.clearAllMocks();
});