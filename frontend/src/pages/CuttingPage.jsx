import { useState } from "react";

import {
  calculateCutting,
} from "../api/cutting";

import CuttingForm from "../components/CuttingForm";
import CuttingResult from "../components/CuttingResult";
import InventoryTable from "../components/InventoryTable";


function CuttingPage() {
  const [result, setResult] =
    useState(null);

  const [loading, setLoading] =
    useState(false);

  const [error, setError] =
    useState(null);


  async function handleCalculate(data) {
    setLoading(true);
    setError(null);

    try {
      const response =
        await calculateCutting(data);

      setResult(response);
    } catch (error) {
      setError(error.message);
    } finally {
      setLoading(false);
    }
  }


  return (
    <div className="app">
      <header className="header">
        <div>
          <h1>CutTracker</h1>

          <p>
            Система учета и расчета
            раскроя листового металла
          </p>
        </div>
      </header>

      <main className="container">
        <CuttingForm
          onCalculate={handleCalculate}
          loading={loading}
        />

        {error && (
          <div className="error-message">
            {error}
          </div>
        )}

        <CuttingResult
          result={result}
        />

        <InventoryTable />
      </main>
    </div>
  );
}


export default CuttingPage;