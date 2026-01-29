function PartsTable({
  parts,
  onChange,
  onRemove,
}) {
  function updatePart(
    index,
    field,
    value
  ) {
    const updatedParts = [...parts];

    updatedParts[index] = {
      ...updatedParts[index],
      [field]: value,
    };

    onChange(updatedParts);
  }


  return (
    <div className="parts-table">
      <div className="section-header">
        <h2>Детали</h2>

        <button
          type="button"
          onClick={() =>
            onChange([
              ...parts,
              {
                name: "",
                width: 0,
                height: 0,
                quantity: 1,
              },
            ])
          }
        >
          Добавить деталь
        </button>
      </div>

      <table>
        <thead>
          <tr>
            <th>Название</th>
            <th>Ширина</th>
            <th>Высота</th>
            <th>Количество</th>
            <th></th>
          </tr>
        </thead>

        <tbody>
          {parts.map((part, index) => (
            <tr key={index}>
              <td>
                <input
                  value={part.name}
                  onChange={(event) =>
                    updatePart(
                      index,
                      "name",
                      event.target.value
                    )
                  }
                  placeholder="Название"
                />
              </td>

              <td>
                <input
                  type="number"
                  min="1"
                  value={part.width}
                  onChange={(event) =>
                    updatePart(
                      index,
                      "width",
                      Number(event.target.value)
                    )
                  }
                />
              </td>

              <td>
                <input
                  type="number"
                  min="1"
                  value={part.height}
                  onChange={(event) =>
                    updatePart(
                      index,
                      "height",
                      Number(event.target.value)
                    )
                  }
                />
              </td>

              <td>
                <input
                  type="number"
                  min="1"
                  value={part.quantity}
                  onChange={(event) =>
                    updatePart(
                      index,
                      "quantity",
                      Number(event.target.value)
                    )
                  }
                />
              </td>

              <td>
                <button
                  type="button"
                  className="danger-button"
                  onClick={() =>
                    onRemove(index)
                  }
                >
                  Удалить
                </button>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}


export default PartsTable;