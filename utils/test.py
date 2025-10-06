def test(file_name: str, test_results: list, results: list) -> None:

    print(file_name)

    errors = []

    for idx, (test_result, result) in enumerate(zip(test_results, results)):

        if test_result != result:
            errors.append(f"{chr(0x274C)} Ошибка. Тестовый кейс {idx + 1}")

    if not errors:
        errors.append(f"{chr(0x2705)} Успех")

    print('\n'.join(errors))
    