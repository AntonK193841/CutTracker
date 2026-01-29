import { useState } from "react";

import PartsTable from "./PartsTable";


function CuttingForm({
  onCalculate,
  loading,
}) {
  const [sheetWidth, setSheetWidth] =
    useState(2000);

  const [sheetHeight, setSheetHeight] =
    useState(6000);

  const [materialId, setMaterialId] =
    useState(1);

  const [parts, setParts] = useState([
    {
      name: "Bottom Plate",
      width: 500,
      height: 1000,
      quantity: 2,
    },
  ]);


  function removePart(index) {
    setParts(
      parts.filter(
        (_, partIndex) =>
          partIndex !== index
      )
    );
  }


  function handleSubmit(event) {
    event.preventDefault();

    onCalculate({
      material_id: Number(materialId),
      sheet_width: Number(sheetWidth),
      sheet_height: Number(sheetHeight),
      parts: parts.map((part) => ({
        name: part.name,
        width: Number(part.width),
        height: Number(part.height),
        quantity: Number(part.quantity),
      })),
    });
  }


  return (
    <form
      className="cutting-form"
      onSubmit={handleSubmit}
    >
      <div className="sheet-settings">
        <h2>Параметры листа</h2>

        <div className="form-grid">
          <label>
            ID материала

            <input
              type="number"
              min="1"
              value={materialId}
              onChange={(event) =>
                setMaterialId(
                  event.target.value
                )
              }
            />
          </label>

          <label>
            Ширина, мм

            <input
              type="number"
              min="1"
              value={sheetWidth}
              onChange={(event) =>
                setSheetWidth(
                  event.target.value
                )
              }
            />
          </label>

          <label>
            Высота, мм

            <input
              type="number"
              min="1"
              value={sheetHeight}
              onChange={(event) =>
                setSheetHeight(
                  event.target.value
                )
              }
            />
          </label>
        </div>
      </div>

      <PartsTable
        parts={parts}
        onChange={setParts}
        onRemove={removePart}
      />

      <button
        className="calculate-button"
        type="submit"
        disabled={loading}
      >
        {loading
          ? "Расчёт..."
          : "Рассчитать раскрой"}
      </button>
    </form>
  );
}


export default CuttingForm;