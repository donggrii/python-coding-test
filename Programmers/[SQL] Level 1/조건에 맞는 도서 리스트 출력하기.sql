-- SELECT - 조건에 맞는 도서 리스트 출력하기 (Oracle)

-- 내 풀이
SELECT BOOK_ID,
       TO_CHAR(PUBLISHED_DATE, 'YYYY-MM-DD') AS PUBLISHED_DATE
FROM BOOK
WHERE CATEGORY = '인문' AND TO_CHAR(PUBLISHED_DATE, 'YYYY') = '2021'
-- WHERE CATEGORY = '인문' AND EXTRACT(YEAR FROM PUBLISHED_DATE) = '2021'
ORDER BY PUBLISHED_DATE;