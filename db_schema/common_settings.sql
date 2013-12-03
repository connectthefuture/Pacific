--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';

-- This controls whether ordinary string literals ('...')
-- treat backslashes literally, as specified in the SQL standard.
-- The default is currently off, causing PostgreSQL to have its
-- historical behavior of treating backslashes as escape characters.
-- The default will change to on in a future release to improve
-- compatibility with the standard. Applications may check this
-- parameter to determine how string literals will be processed.
-- The presence of this parameter can also be taken as an indication
-- that the escape string syntax (E'...') is supported.
-- Escape string syntax should be used if an application desires
-- backslashes to be treated as escape characters.
SET standard_conforming_strings = on;

-- When on, a warning is issued if a backslash (\) appears in an
-- ordinary string literal ('...' syntax) and
-- standard_conforming_strings is off. The default is on.
-- Applications that wish to use backslash as escape should be
-- modified to use escape string syntax (E'...'), because the default
-- behavior of ordinary strings will change in a future release for
-- SQL compatibility. This variable can be enabled to help detect
-- applications that will break.
SET escape_string_warning = on;

SET check_function_bodies = false;
SET client_min_messages = warning;


-- Create a schema owned by gamefragtion_master
CREATE SCHEMA pacific AUTHORIZATION pacific_master;
-- Do not use public schema!
SET search_path = "$user", pg_catalog;


SET default_tablespace = '';
-- Using OIDs in new applications is not recommended: where possible,
-- using a SERIAL or other sequence generator as the table's primary key
-- is preferred.
SET default_with_oids = false;
