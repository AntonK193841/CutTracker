import { apiRequest } from "./client";


export function calculateCutting(data) {
  return apiRequest(
    "/api/cutting/calculate",
    {
      method: "POST",
      body: JSON.stringify(data),
    }
  );
}


export function getCuttingPlans() {
  return apiRequest(
    "/api/cutting/plans"
  );
}