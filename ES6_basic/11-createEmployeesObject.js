export default function createEmployeesObject(departmentName, employees) {
  const employeObject = {
    [departmentName]: [...employees],
  };
  return employeObject;
}
