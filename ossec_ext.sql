CREATE VIEW rule_category_view AS SELECT category.cat_id, category.cat_name, signature_category_mapping.rule_id
FROM category, signature_category_mapping WHERE category.cat_id = signature_category_mapping.cat_id;


CREATE VIEW rule_view AS SELECT rule_id,
array_agg((SELECT cat_name FROM category WHERE cat_id = signature_category_mapping.cat_id)) AS categories
FROM signature_category_mapping GROUP BY rule_id;


CREATE VIEW category_view AS SELECT category.cat_id, category.cat_name,
array_agg(signature_category_mapping.rule_id) AS rules
FROM category, signature_category_mapping WHERE signature_category_mapping.cat_id = category.cat_id
GROUP BY category.cat_id;
