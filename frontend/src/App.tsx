import React from 'react';
import { motion } from 'framer-motion';

function App() {
  return (
    <motion.div
      initial={{ opacity: 0 }}
      animate={{ opacity: 1 }}
      exit={{ opacity: 0 }}
    >
      <h1>AI-Driven Personalization Engine</h1>
    </motion.div>
  );
}

export default App;
