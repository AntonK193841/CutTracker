import { apiRequest } from "./client";


export function getMaterials() {
  return apiRequest(
    "/api/materials"
  );
}