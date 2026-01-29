import PlacementCanvas from "./PlacementCanvas";


function CuttingResult({
  result,
}) {
  if (!result) {
    return null;
  }


  return (
    <section className="result-section">
      <h2>Результат расчёта</h2>

      <div className="statistics">
        <div className="stat-card">
          <span>Площадь листа</span>
          <strong>
            {result.sheet_area.toLocaleString()}
          </strong>
          <small>мм²</small>
        </div>

        <div className="stat-card">
          <span>Площадь деталей</span>
          <strong>
            {result.placed_area.toLocaleString()}
          </strong>
          <small>мм²</small>
        </div>

        <div className="stat-card">
          <span>Отходы</span>
          <strong>
            {result.waste_area.toLocaleString()}
          </strong>
          <small>мм²</small>
        </div>

        <div className="stat-card">
          <span>Использование</span>
          <strong>
            {result.utilization.toFixed(2)}%
          </strong>
          <small>материала</small>
        </div>
      </div>

      <PlacementCanvas
        result={result}
      />

      {result.unplaced_parts.length > 0 && (
        <div className="unplaced-section">
          <h3>
            Детали, которые не удалось разместить
          </h3>

          <ul>
            {result.unplaced_parts.map(
              (part, index) => (
                <li key={index}>
                  {part.name} —{" "}
                  {part.width} ×{" "}
                  {part.height} мм
                </li>
              )
            )}
          </ul>
        </div>
      )}
    </section>
  );
}


export default CuttingResult;