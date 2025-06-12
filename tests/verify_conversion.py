from datetime import date as gregorian_date


try:
    from bikram_sambat import conversion
    from bikram_sambat.exceptions import (
        DateOutOfRangeError,
        InvalidDateError,
        InvalidTypeError,
    )
except ImportError:
    print("ERROR: Could not import the 'bikram_sambat' package.")
    print("Ensure it's installed or the PYTHONPATH is set correctly.")
    print(
        "If running this script from within the project root, you might need to adjust imports (e.g., 'from . import conversion') if it's part of the package, or ensure the package is installed in editable mode."
    )
    exit()


TEST_DATA_PAIRS = [
    (gregorian_date(1844, 4, 11), (1901, 1, 1)),
    (gregorian_date(1844, 4, 12), (1901, 1, 2)),
    (gregorian_date(1844, 5, 11), (1901, 1, 31)),
    (gregorian_date(1844, 5, 12), (1901, 2, 1)),
    (gregorian_date(2023, 10, 26), (2080, 7, 9)),
    (gregorian_date(2024, 1, 1), (2080, 9, 16)),
    (
        gregorian_date(1944, 4, 10),
        (2000, 12, 31),
    ),  # AD 1944-04-10 <-> BS 2000-12-31 (Chaitra has 31 days)
    (gregorian_date(1944, 4, 11), (2001, 1, 1)),  # AD 1944-04-11 <-> BS 2001-01-01
    (gregorian_date(1993, 9, 5), (2050, 5, 20)),
    (gregorian_date(2141, 5, 15), (2198, 1, 30)),
    (gregorian_date(2143, 5, 24), (2199, 12, 30)),
    (gregorian_date(1980, 7, 16), (2037, 4, 1)),
    (gregorian_date(2000, 1, 25), (2056, 10, 11)),
    (gregorian_date(2040, 3, 1), (2096, 11, 18)),
    (gregorian_date(1956, 2, 29), (2012, 11, 17)),
    (gregorian_date(2065, 12, 31), (2122, 9, 17)),
    (gregorian_date(1860, 6, 20), (1917, 3, 7)),
    (gregorian_date(2025, 5, 18), (2082, 2, 4)),
    (gregorian_date(1900, 1, 1), (1956, 9, 18)),
    (gregorian_date(2000, 1, 1), (2056, 9, 17)),
    (gregorian_date(1845, 1, 1), (1901, 9, 17)),
    (gregorian_date(1846, 7, 4), (1903, 3, 21)),
    (gregorian_date(1847, 11, 30), (1904, 8, 16)),
    (gregorian_date(1848, 5, 1), (1905, 1, 18)),
    (gregorian_date(1849, 9, 10), (1906, 5, 27)),
    (gregorian_date(1850, 2, 22), (1906, 11, 11)),
    (gregorian_date(1851, 8, 1), (1908, 4, 18)),
    (gregorian_date(1852, 12, 15), (1909, 9, 1)),
    (gregorian_date(1853, 6, 2), (1910, 2, 19)),
    (gregorian_date(1854, 10, 18), (1911, 7, 4)),
    (gregorian_date(1855, 3, 7), (1911, 11, 23)),
    (gregorian_date(1856, 9, 2), (1913, 5, 20)),
    (gregorian_date(1857, 1, 19), (1913, 10, 6)),
    (gregorian_date(1858, 7, 25), (1915, 4, 11)),
    (gregorian_date(1859, 11, 8), (1916, 7, 24)),
    (gregorian_date(1860, 4, 1), (1916, 12, 19)),
    (gregorian_date(1861, 10, 1), (1918, 6, 17)),
    (gregorian_date(1862, 3, 17), (1918, 11, 2)),
    (gregorian_date(1863, 9, 11), (1920, 5, 28)),
    (gregorian_date(1864, 2, 28), (1920, 11, 15)),
    (gregorian_date(1865, 8, 14), (1922, 4, 30)),
    (gregorian_date(1866, 12, 29), (1923, 9, 15)),
    (gregorian_date(1867, 6, 16), (1924, 3, 4)),
    (gregorian_date(1868, 11, 1), (1925, 7, 18)),
    (gregorian_date(1869, 4, 18), (1926, 1, 4)),
    (gregorian_date(1870, 10, 5), (1927, 6, 21)),
    (gregorian_date(1871, 3, 20), (1927, 11, 6)),
    (gregorian_date(1872, 9, 1), (1929, 5, 19)),
    (gregorian_date(1873, 2, 15), (1929, 10, 5)),
    (gregorian_date(1874, 8, 10), (1931, 4, 21)),
    (gregorian_date(1875, 1, 24), (1931, 10, 10)),
    (gregorian_date(1876, 7, 1), (1933, 3, 19)),
    (gregorian_date(1877, 12, 10), (1934, 8, 27)),
    (gregorian_date(1878, 5, 27), (1935, 2, 14)),
    (gregorian_date(1879, 10, 13), (1935, 7, 28)),
    (gregorian_date(1880, 4, 29), (1937, 1, 16)),
    (gregorian_date(1881, 9, 2), (1938, 5, 20)),
    (gregorian_date(1882, 2, 18), (1938, 10, 5)),
    (gregorian_date(1883, 8, 7), (1940, 4, 24)),
    (gregorian_date(1884, 1, 22), (1940, 9, 9)),
    (gregorian_date(1885, 7, 15), (1942, 3, 2)),
    (gregorian_date(1886, 12, 1), (1943, 8, 19)),
    (gregorian_date(1887, 5, 10), (1944, 2, 27)),
    (gregorian_date(1888, 10, 26), (1945, 7, 10)),
    (gregorian_date(1889, 3, 11), (1945, 11, 27)),
    (gregorian_date(1890, 9, 20), (1947, 5, 15)),
    (gregorian_date(1891, 2, 5), (1947, 10, 22)),
    (gregorian_date(1892, 8, 1), (1949, 4, 17)),
    (gregorian_date(1893, 1, 17), (1949, 9, 4)),
    (gregorian_date(1894, 7, 12), (1951, 2, 20)),
    (gregorian_date(1895, 12, 28), (1952, 8, 13)),
    (gregorian_date(1896, 6, 14), (1953, 2, 1)),
    (gregorian_date(1897, 11, 30), (1954, 7, 17)),
    (gregorian_date(1898, 5, 16), (1955, 1, 3)),
    (gregorian_date(1899, 10, 1), (1955, 6, 18)),
    (gregorian_date(1900, 4, 17), (1957, 1, 4)),
    (gregorian_date(2088, 1, 29), (2144, 9, 16)),
]


def run_tests():
    passed_count = 0
    failed_count = 0
    error_count = 0
    total_tests = 0

    print("--- Testing AD to BS Conversions ---")
    for i, (ad_date, expected_bs_tuple) in enumerate(TEST_DATA_PAIRS):
        total_tests += 1
        test_id = f"AD_BS_Pair_{i+1:03d}"
        print(
            f"\n[{test_id}] Input AD: {ad_date.isoformat()}, Expected BS: {expected_bs_tuple}"
        )
        try:
            actual_bs_tuple = conversion.ad_to_bs(ad_date)
            if actual_bs_tuple == expected_bs_tuple:
                print(f"  PASS: Actual BS: {actual_bs_tuple}")
                passed_count += 1
            else:
                print(
                    f"  FAIL: Actual BS: {actual_bs_tuple} (Expected: {expected_bs_tuple})"
                )
                failed_count += 1
        except (DateOutOfRangeError, InvalidDateError, InvalidTypeError) as e:
            print(f"  ERROR during ad_to_bs: {type(e).__name__}: {e}")
            error_count += 1
        except Exception as e:
            print(f"  UNEXPECTED ERROR during ad_to_bs: {type(e).__name__}: {e}")
            error_count += 1

    print("\n--- Testing BS to AD Conversions ---")
    for i, (expected_ad_date, bs_tuple) in enumerate(TEST_DATA_PAIRS):
        total_tests += 1
        test_id = f"BS_AD_Pair_{i+1:03d}"
        bs_y, bs_m, bs_d = bs_tuple
        print(
            f"\n[{test_id}] Input BS: {bs_tuple}, Expected AD: {expected_ad_date.isoformat()}"
        )
        try:
            actual_ad_date = conversion.bs_to_ad(bs_y, bs_m, bs_d)
            if actual_ad_date == expected_ad_date:
                print(f"  PASS: Actual AD: {actual_ad_date.isoformat()}")
                passed_count += 1
            else:
                print(
                    f"  FAIL: Actual AD: {actual_ad_date.isoformat()} (Expected: {expected_ad_date.isoformat()})"
                )
                failed_count += 1
        except (DateOutOfRangeError, InvalidDateError, InvalidTypeError) as e:
            print(f"  ERROR during bs_to_ad: {type(e).__name__}: {e}")

            error_count += 1
        except Exception as e:
            print(f"  UNEXPECTED ERROR during bs_to_ad: {type(e).__name__}: {e}")
            error_count += 1

    print("\n--- Testing Round Trip AD -> BS -> AD ---")
    for i, (ad_original, _) in enumerate(TEST_DATA_PAIRS):
        total_tests += 1
        test_id = f"RT_AD_BS_AD_Pair_{i+1:03d}"
        print(
            f"\n[{test_id}] Round Trip AD->BS->AD for Original AD: {ad_original.isoformat()}"
        )
        try:
            bs_y, bs_m, bs_d = conversion.ad_to_bs(ad_original)
            ad_round_trip = conversion.bs_to_ad(bs_y, bs_m, bs_d)
            if ad_round_trip == ad_original:
                print(
                    f"  PASS: Round trip consistent. BS: ({bs_y},{bs_m},{bs_d}), AD' : {ad_round_trip.isoformat()}"
                )
                passed_count += 1
            else:
                print(
                    f"  FAIL: Round trip inconsistent. BS: ({bs_y},{bs_m},{bs_d}), AD': {ad_round_trip.isoformat()} (Original AD: {ad_original.isoformat()})"
                )
                failed_count += 1
        except (DateOutOfRangeError, InvalidDateError, InvalidTypeError) as e:
            print(f"  ERROR during AD->BS->AD round trip: {type(e).__name__}: {e}")
            error_count += 1
        except Exception as e:
            print(
                f"  UNEXPECTED ERROR during AD->BS->AD round trip: {type(e).__name__}: {e}"
            )
            error_count += 1

    print("\n--- Testing Round Trip BS -> AD -> BS ---")
    for i, (_, bs_original_tuple) in enumerate(TEST_DATA_PAIRS):
        total_tests += 1
        bs_y_orig, bs_m_orig, bs_d_orig = bs_original_tuple
        test_id = f"RT_BS_AD_BS_Pair_{i+1:03d}"
        print(
            f"\n[{test_id}] Round Trip BS->AD->BS for Original BS: {bs_original_tuple}"
        )
        try:
            ad_converted = conversion.bs_to_ad(bs_y_orig, bs_m_orig, bs_d_orig)
            bs_rt_y, bs_rt_m, bs_rt_d = conversion.ad_to_bs(ad_converted)
            bs_round_trip_tuple = (bs_rt_y, bs_rt_m, bs_rt_d)

            if bs_round_trip_tuple == bs_original_tuple:
                print(
                    f"  PASS: Round trip consistent. AD: {ad_converted.isoformat()}, BS': {bs_round_trip_tuple}"
                )
                passed_count += 1
            else:
                print(
                    f"  FAIL: Round trip inconsistent. AD: {ad_converted.isoformat()}, BS': {bs_round_trip_tuple} (Original BS: {bs_original_tuple})"
                )
                failed_count += 1
        except (DateOutOfRangeError, InvalidDateError, InvalidTypeError) as e:
            print(f"  ERROR during BS->AD->BS round trip: {type(e).__name__}: {e}")
            error_count += 1
        except Exception as e:
            print(
                f"  UNEXPECTED ERROR during BS->AD->BS round trip: {type(e).__name__}: {e}"
            )
            error_count += 1

    print("\n--- Test Summary ---")
    print(f"Total checks run: {total_tests}")
    print(f"Passed: {passed_count}")
    print(f"Failed: {failed_count}")
    print(f"Errors (exceptions during conversion): {error_count}")
    if failed_count == 0 and error_count == 0:
        print("\nALL CHECKS PASSED SUCCESSFULLY!")
    else:
        print("\nSOME CHECKS FAILED OR ERRORED. Please review the output above.")


if __name__ == "__main__":
    print("Starting Bikram Sambat conversion verification...")
    print(
        "Make sure your TEST_DATA_PAIRS are verified and accurate for your calendar system."
    )
    print(
        "This script assumes pairs are for valid, in-range dates unless an error is expected by design."
    )
    print("-" * 70)
    run_tests()
