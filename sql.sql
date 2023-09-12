CREATE TABLE IF NOT EXISTS employes
(
    id integer NOT NULL DEFAULT nextval('employes_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    surname character varying(100) COLLATE pg_catalog."default" NOT NULL,
    "position" character varying(50) COLLATE pg_catalog."default",
    company_id integer NOT NULL,
    CONSTRAINT employes_pkey PRIMARY KEY (id),
    CONSTRAINT fk_employee_company FOREIGN KEY (company_id)
        REFERENCES public.companies (id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
);
CREATE TABLE IF NOT EXISTS companies
(
    id integer NOT NULL DEFAULT nextval('companies_id_seq'::regclass),
    name character varying(100) COLLATE pg_catalog."default" NOT NULL,
    address character varying(255) COLLATE pg_catalog."default" NOT NULL,
    CONSTRAINT companies_pkey PRIMARY KEY (id)
);

INSERT INTO companies(name, address)  VALUES
                                           ('Xiaomi', 'China Hong Kong'),
                                           ('Google', 'USA California');

INSERT INTO employes(name, surname, position, company_id)  VALUES
                                                               ('Danila', 'Myakotin', 'Ml-ops', 1),
                                                               ('Danil', 'Klochkov', 'full stack', 2),
                                                               ('Dmitry', 'Starikov', 'Researcher', 2),
                                                               ('Ivan', 'Bragin', 'Devops', 1),
                                                               ('Danil', 'Zgonik', 'Data Scientist', 2);