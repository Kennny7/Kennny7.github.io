import { defineCollection, z } from 'astro:content';

const projectsCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(),
    image: z.string().optional(),
    github: z.string().url(),
    demo: z.string().url().optional(),
    tags: z.array(z.string()).default([]),
    featured: z.boolean().default(true),
    fetchGithubData: z.boolean().default(false),
    order: z.number().default(0),
  }),
});

const experienceCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    company: z.string(),
    startDate: z.string(),
    endDate: z.string().optional(),
    tags: z.array(z.string()).default([]),
    featured: z.boolean().default(true),
    order: z.number().default(0),
    logo: z.string().optional(),            
    summary: z.string().optional(), 
  }),
});

export const collections = {
  projects: projectsCollection,
  experience: experienceCollection,
};