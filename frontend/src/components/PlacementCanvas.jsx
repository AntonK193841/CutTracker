function PlacementCanvas({
  result,
}) {
  if (!result) {
    return null;
  }


  const sheetWidth =
    result.sheet_width;

  const sheetHeight =
    result.sheet_height;


  function getStyle(placement) {
    return {
      left: `${(
        placement.x /
        sheetWidth
      ) * 100}%`,

      top: `${(
        placement.y /
        sheetHeight
      ) * 100}%`,

      width: `${(
        placement.width /
        sheetWidth
      ) * 100}%`,

      height: `${(
        placement.height /
        sheetHeight
      ) * 100}%`,
    };
  }


  return (
    <div className="placement-section">
      <h2>Схема раскроя</h2>

      <div className="sheet-wrapper">
        <div className="sheet">
          {result.placements.map(
            (placement, index) => (
              <div
                key={index}
                className="placement"
                style={getStyle(
                  placement
                )}
                title={
                  placement.part_name
                }
              >
                <span>
                  {placement.part_name}
                </span>
              </div>
            )
          )}
        </div>
      </div>
    </div>
  );
}


export default PlacementCanvas;