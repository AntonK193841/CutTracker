function InventoryTable({
  materials = [],
  loading = false,
}) {
  return (
    <section className="inventory-section">
      <div className="section-header">
        <h2>Склад материалов</h2>
      </div>

      {loading ? (
        <div className="empty-state">
          Загрузка материалов...
        </div>
      ) : materials.length === 0 ? (
        <div className="empty-state">
          Материалы пока не загружены
        </div>
      ) : (
        <table>
          <thead>
            <tr>
              <th>ID</th>
              <th>Материал</th>
              <th>Марка</th>
              <th>Толщина</th>
              <th>Размер</th>
              <th>Количество</th>
            </tr>
          </thead>

          <tbody>
            {materials.map((material) => (
              <tr key={material.id}>
                <td>{material.id}</td>

                <td>{material.name}</td>

                <td>{material.grade}</td>

                <td>
                  {material.thickness} мм
                </td>

                <td>
                  {material.width} ×{" "}
                  {material.height} мм
                </td>

                <td>
                  {material.quantity}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      )}
    </section>
  );
}


export default InventoryTable;