import os
import redis

REDIS_HOST = os.getenv("REDIS_HOST")
REDIS_PORT = int(os.getenv("REDIS_PORT", 11668))
REDIS_PASSWORD = os.getenv("REDIS_PASSWORD")

r = redis.Redis(
    host='redis-11668.crce218.eu-central-1-1.ec2.cloud.redislabs.com',
    port=11668,
    decode_responses=True,
    username="default",
    password="8FXQ1Zrzs9tAnKWZD12Na86rvnzCUynS",
)

def main():

    r.set("favorite_car", "Audi Q8")
    print("favorite_car:", r.get("favorite_car"))

    two_hours_seconds = 2 * 60 * 60
    r.setex("favorite_pet", two_hours_seconds, "Dog")
    ttl_pet = r.ttl("favorite_pet")
    print("favorite_pet:", r.get("favorite_pet"), "TTL:", ttl_pet)

    products_key = "products_list"
    r.delete(products_key)
    r.rpush(products_key, "bread", "milk", "eggs", "sugar")
    print("products_list:", r.lrange(products_key, 0, -1))

    seven_days_seconds = 7 * 24 * 60 * 60
    r.expire(products_key, seven_days_seconds)
    print("TTL products_list:", r.ttl(products_key))

    cake_key = "cake_ingredients"
    cake_ingredients = {"flour": 250, "milk": 500}
    r.hset(cake_key, mapping=cake_ingredients)
    print("cake_ingredients:", r.hgetall(cake_key))

    r.hset(cake_key, "sugar", 300)
    print("cake_ingredients + sugar=300g:", r.hgetall(cake_key))

    r.hset(cake_key, "sugar", 500)
    print("cake_ingredients sugar=500g:", r.hgetall(cake_key))

    r.delete(cake_key)
    print("cake_ingredients exists?:", r.exists(cake_key))

if __name__ == "__main__":
    main()


    import redis



    success = r.set('foo', 'bar')

    result = r.get('foo')
    print(result)
