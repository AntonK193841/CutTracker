import { useEffect, useState } from "react";

import {
  calculateCutting,
} from "../api/cutting";

import {
  getMaterials,
} from "../api/materials";

import CuttingForm from "../components/CuttingForm";
import CuttingResult from "../components/CuttingResult";
import InventoryTable from "../components/InventoryTable";


function CuttingPage() {
  const [result, setResult] =
    useState(null);

  const [materials, setMaterials] =
    useState([]);

  const [loading, setLoading] =
    useState(false);

  const [materialsLoading, setMaterialsLoading] =
    useState(true);

  const [error, setError] =
    useState(null);


  useEffect(() => {
    async function loadMaterials() {
      try {
        const data =
          await getMaterials();

        setMaterials(data);
      } catch (error) {
        setError(error.message);
      } finally {
        setMaterialsLoading(false);
      }
    }

    loadMaterials();
  }, []);


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

        <InventoryTable
          materials={materials}
          loading={materialsLoading}
        />
      </main>
    </div>
  );
}


export default CuttingPage;