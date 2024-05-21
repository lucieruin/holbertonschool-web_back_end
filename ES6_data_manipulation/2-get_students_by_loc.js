export default function getStudentsByLocation(ids, city) {
  if (!Array.isArray(ids) && typeof city !== 'string') {
    return [];
  }
  return ids.filter((id) => id.location === city);
}
